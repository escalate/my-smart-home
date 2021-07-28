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
	rm --recursive --force ./roles/
	ansible-galaxy role install \
		--role-file="requirements.yml"

.PHONY: collections
collections:
	rm --recursive --force ./collections/
	ansible-galaxy collection install \
		--requirements-file="requirements.yml"

.PHONY: requirements
requirements: roles collections

.PHONY: test
test: up provision down

.PHONY: lint
lint:
	ec
	yamllint --strict --config-file .yamllint .
	ansible-lint .
	find . -maxdepth 1 -name "*.yml" -not -name "requirements.yml" | xargs -n1 ansible-playbook --inventory="hosts" --syntax-check

.PHONY: bootstrap
bootstrap:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts" \
		--limit="$(ANSIBLE_LIMIT)" \
		bootstrap.yml

.PHONY: update
update:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts" \
		--limit="$(ANSIBLE_LIMIT)" \
		update.yml

.PHONY: deploy
deploy:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts" \
		--limit="$(ANSIBLE_LIMIT)" \
		$(ANSIBLE_PLAYBOOK)
