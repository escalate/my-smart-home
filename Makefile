SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c
ANSIBLE_ARGS ?= $(ANSIBLE_OPTIONS)
ANSIBLE_PLAYBOOK ?= smart_home.yml

ifdef ANSIBLE_GROUP
ANSIBLE_LIMIT := $(ANSIBLE_GROUP)
endif

ifdef ANSIBLE_HOST
ANSIBLE_LIMIT := $(ANSIBLE_HOST)
endif

ifdef ANSIBLE_TAGS
ANSIBLE_ARGS := $(ANSIBLE_ARGS) --tags='$(ANSIBLE_TAGS)'
endif

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
	ansible-galaxy role install \
		--roles-path="roles/" \
		--role-file="requirements.yml"

.PHONY: collections
collections:
	rm --recursive --force ~/.ansible/collections/
	ansible-galaxy collection install \
		--requirements-file="requirements.yml"

.PHONY: requirements
requirements: roles collections

.PHONY: test
test: up provision down

.PHONY: lint
lint:
	yamllint --strict .
	ansible-lint *.yml

.PHONY: deploy
deploy:
	ansible-playbook \
		$(ANSIBLE_ARGS) \
		--inventory="hosts" \
		$(ANSIBLE_PLAYBOOK)
