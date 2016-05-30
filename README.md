rdo
=========

Ansible role to add Openstack  repositories.

It add Ubuntu Cloud Archive on Ubuntu or RDO on EL.


Requirements
------------

None.

Role Variables
--------------

Just define openstack version codename:

    openstack_version: liberty


Example Playbook
----------------


    - hosts: servers
      roles:
         - { role: abelboldu.openstack-repo , openstack_version: liberty  }

License
-------

Apache 2.0

Author Information
------------------

Abel Boldú < abel.boldu (-) gmx.com >
