# Password Policy Analyzer

PPA is a script that lets you search for passwords given different criteria found in password policies such as, use of uppercase or digit.
The script displays the number of passwords that match the criteria and the percentage of the total passwords.

Development enviorment:
- Ubuntu 20.04 64-bit
- Kernel 5.8.0-44-generic
- Python 3.8
 
Packages used can be installed by running
```sh
pip install -r requirements.txt
```

### Example use

```sh
python3 interface.py password_file character_length arguments
python3 interface.py passwords.txt 12 -u -d -s
```
The example searches for passwords with a minimum character length 12 containing at least one uppercase character, one digit, and one special character.
The special characters inlcude " !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

### Example result
!Example use](Images/example_use.png "Example use")