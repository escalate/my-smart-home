SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c
ANSIBLE_ARGS ?= $(ANSIBLE_OPTIONS)
ANSIBLE_PLAYBOOK ?= site.yml

ifdef ANSIBLE_GROUP
ANSIBLE_LIMIT := $(ANSIBLE_GROUP)
endif

ifdef ANSIBLE_HOST
ANSIBLE_LIMIT := $(ANSIBLE_HOST)
endif

ifdef ANSIBLE_TAGS
ANSIBLE_ARGS := $(ANSIBLE_ARGS) --tags='$(ANSIBLE_TAGS)'
endif

.PHONY: version
version:
	ansible --version
	ansible-lint --version
	ec --version
	yamllint --version

.PHONY: up
up:
	vagrant up

.PHONY: provision
provision:
	ANSIBLE_ARGS="$(ANSIBLE_ARGS)" vagrant provision

.PHONY: suspend
suspend:
	vagrant suspend

.PHONY: resume
resume:
	vagrant resume

.PHONY: status
status:
	vagrant status

.PHONY: destroy
destroy:
	vagrant destroy --force

.PHONY: roles
roles:
	rm --recursive --force roles/
	until ansible-galaxy role install \
		--roles-path="roles/" \
		--role-file="requirements.yml"; \
	do \
		echo "Download of Ansible roles failed. Try again"; \
	done

.PHONY: collections
collections:
	rm --recursive --force ~/.ansible/collections/
	until ansible-galaxy collection install \
		--requirements-file="requirements.yml"; \
	do \
		echo "Download of Ansible collections failed. Try again"; \
	done

.PHONY: requirements
requirements: roles collections

.PHONY: test
test: up provision down

.PHONY: lint
lint:
	ec
	yamllint --strict --config-file .yamllint .
	ansible-lint .
ifndef CI
	find . -maxdepth 1 -name "*.yml" -not -name "requirements.yml" | xargs -n1 ansible-playbook --inventory="hosts.yml" --syntax-check
endif

.PHONY: bootstrap
bootstrap:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts.yml" \
		--limit="$(ANSIBLE_LIMIT)" \
		bootstrap.yml

.PHONY: update
update:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts.yml" \
		--limit="$(ANSIBLE_LIMIT)" \
		update.yml

.PHONY: deploy
deploy:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts.yml" \
		--limit="$(ANSIBLE_LIMIT)" \
		$(ANSIBLE_PLAYBOOK)
