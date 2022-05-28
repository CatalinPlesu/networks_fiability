# Network Fiability

## Usage
#### create a  virtual enviroment
```
python -m venv venv
```

### activate virtual enviroment (bash)
```
source venv/bin/activate
```

### activate virtual enviroment (windows power shell)
```
source venv/bin/Activate.ps1
```

#### installation dependencies
```
pip install -r requirements.txt
```

### execution
```
python main.py

```

## CLI arguments
```
options:
  -h, --help           show this help message and exit
  -m int               Numarul de subretele,
                       m implicit - 50
  -n int               Numarul de elemente in subretela,
                       n implicit - 50
  --n_non_const        n va varia in fiecare subretela

  --no_gui             terminal mode

  --distribution Nume  Tipul distributiei aplicate elementelor retelei,
                       optiuni: Normal, Poisson, Uniform, ...
                       implicit - Normal
```
