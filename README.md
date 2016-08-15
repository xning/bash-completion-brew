About
=====

The brew completion is just a copy of the koji completion.

The brew completion target users most possibly use one of the OSs:

- Fedora2X
- RHEL6/CentOS6
- and RHEL7/CentOS7

Hence we need the brew completion to support these OSs.

But the available bash-completions for these OSs are different


| Repo     | Fedora2X           | RHEL6                   | RHEL7                   |
|:--------:|:------------------:| ----------------------: |:-----------------------:|
| EPEL     | N/A                | bash-completion-1.3¹    | N/A                     |
| Official | bash-compltion-2.1 | N/A                     | bash-completion-2.1²    |
| Brew     | N/A                | bash-completion-2.1     | N/A                     |
1: package doesn't support the koji completion.    
2: package doesn't have the koji completion.

Hence, we need at least express the following requirements

- we need bash-completion-2.1 on RHEL6 and CentOS6.
- we need the koji compleiton on RHEL7 and CentOS7.
- brew completion is a copy of koji completion.

On the other way, I hope the brew completion is "normal" enough, so

- the brewkoji package dosn't require bash-completion.
- the brew completion is not enabled after installing.
- following bash-completion guide, a user could enable/disable
  the brew completion.
- in the more latest system, the brew completion will be automatically loaded
  when users type 'brew' command.

Because of the above concerns, I prepared this simple RPM package.

For more details, please browse the following links

1. Why does not RHEL7 support koji completion?
https://bugzilla.redhat.com/show_bug.cgi?id=810343

2. For bash-completion
http://bash-completion.alioth.debian.org/

Seems this url will redirect to a github.com.
