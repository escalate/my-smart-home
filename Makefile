SHELL = /bin/bash -eo pipefail
ANSIBLE_ARGS ?= $(ANSIBLE_OPTIONS)
ANSIBLE_PLAYBOOK ?= smart_home.yml

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

.PHONY: requirements
requirements:
	rm --recursive --force roles/
	ansible-galaxy install \
		--roles-path="roles/" \
		--role-file="requirements.yml" \
		--ignore-errors

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
