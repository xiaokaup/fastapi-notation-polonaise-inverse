# fastapi-notation-polonaise-inverse

## Command

Build Frontend and Backend docker images

```bash
./build.sh
```

Run Frontend and Backend docker images

```bash
./run.sh
```

Build and run

```bash
./build.sh && ./run.sh
```

## Backend

Endpoint: http://localhost:8000/

Routes:

- POST http://localhost:8000/calculator/
- GET http://localhost:8000/get_results/
- GET http://localhost:8000/get_csv_data

### Test

Test files location: ./backend/tests

```bash
cd backend
./test.sh
```

## Frontend

Endpoint: http://localhost:3000/

## Database

sqlite: ./backend/calculator.db

If you want to clean historical results:

```bash
rm ./backend/calculator.db
```

## NPI(notation polonaise inverse) Calculate

we can write the

- number `1`, `2`, `3`, like

```text
1 2 + 3 /
```

- number started by `0`, `01`, `02`, `03`, like

```text
01 02 + 03 /
```

- number more than 1 digital: `10`, `20`, `100`, `1000`, like

```text
10 20 + 100 - 1000 *
```

- express with randomly space ` `, like

```text
10       20 +       100 -  1000   *
```

- negative number `-10`, `-01`, like

```text
-10     -01 +
```

## Author

Github profil: https://github.com/xiaokaup  
Website: https://wemediaweb.com/fr/home-fr/
