# ur-state-receiver

## Overview
Simple Python3 modul to receive data from Universal Robots and write out to console.
This version is compatible with controller version 3.11

**NOTE**: It is an experimental software. Do not use this in production systems!

THE SOFTWARE IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT WITHOUT ANY WARRANTY. IT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

## Overview
1. [Requirements](#requirements)
2. [Parameters](#parameters)
3. [Example usage](#example-usage)
4. [Bugs, feature requests, etc](#bugs-feature-requests-etc)

### Requirements
Install **Python3**.

### Parameters

Before you run this module, you have to adjust these parameters in main.py:

- HOST
>*(e.g. 192.168.56.101)*
- PORT
>*(e.g. 30003)*
- TIMEOUT
>*(e.g. 2)*

### Example usage
Unix:
```
python ./main.py
```
Windows:
```
python .\main.py
```

## Bugs, feature requests, etc
Please use the GitHub issue tracker.