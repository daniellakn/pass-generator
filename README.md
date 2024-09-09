# Strong Password Generator

Command-line interface tool that generates strong random passwords. By default, 3 passwords of 16 characters each, are generated, without replacement. <br>
This tool utilises the Python secrets library, since it is cryptographically secure.

The length of the password is set using the `-l`/`--length` switch.

The number of passwords generated is set using the `-n`/`--number` switch. 

A custom charset can be set using the `-i`/`--include` switch.

To exclude characters from the default charset, use the `-e`/`--exclude` switch.

Instead of outputting the generated password to the terminal, the password can also be directly copied to clipboard using the `-c`/`--copy` switch.


## Example Usage:

```
$ python3 src/main.py -l 30 -n 1 -e "\'\""
```
*Output:* `Password 1: Qm#7w{:0^cfS@6;r*v14*>y?7W<8i1`

<br>

```
$ python3 src/main.py -i "QWERTY0123456789" -c
```
*Output*: `Password copied to clipboard.` <br>
*Clipboard*: `90987R2093EYYQ4Y`
