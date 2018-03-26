#!/bin/bash
ansible-playbook -vv ./deploy.yml --private-key=/Users/jared/.ssh/id_rsa -u deployer -i ./hosts