# factor-loom

Show the prime factorization of a signed integer, with repeated factors grouped as powers.

## Use

Requires Python 3.10+; no packages to install.

```sh
python factor_loom.py 360
python factor_loom.py -84
python factor_loom.py 1
```

Zero is rejected because it has no finite prime factorization. Inputs are limited to an absolute value of 1,000,000,000,000 so trial division stays bounded. Negative inputs include `-1` as a factor.

## License

MIT
