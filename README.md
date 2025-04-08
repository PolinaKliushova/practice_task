# Проект моделирования разрушения цилиндра с использованием Peridigm и Docker

## Описание

Проект моделирует разрушение цилиндра методом перидинамики (Peridigm) с использованием контейнеризации Docker.

Основные этапы:
1. Генерация сетки цилиндра с помощью `cylinder_generator.py`.
2. Конфигурация модели через файл `pull.yaml`.
3. Запуск моделирования в контейнере Peridigm через Docker Compose.
4. Просмотр результатов в ParaView.
5. Преобразование и анализ данных с помощью `preprocess.py`.

---

## Установка и запуск

1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2. Клонируйте репозиторий:

```bash
git clone <ссылка_на_репозиторий>
cd prak
```

3. Запустите контейнер:

```bash
docker-compose up
```

4. Сгенерируйте данные:

```bash
python data/cylinder_generator.py
```

5. Запустите моделирование:

```bash
docker-compose exec peridigm mpiexec -np 1 Peridigm data/pull.yaml
```

---

## Структура проекта

```
prak/
│
├── data/
│   ├── cylinder_generator.py                # Скрипт генерации сетки
│   ├── pull.yaml                            # Конфигурация для Peridigm
│
├── docker-compose.yml                       # Docker-контейнер с Peridigm
├── preprocess.py                            # Преобразование выходных данных
├── README.md                                # Документация
```

---

## Выходные данные

- `fragmenting_cylinder.txt` — координаты точек и параметры.
- `fragmenting_cylinder_nodeset.txt` — узлы для начальных условий.
- `fragmenting_cylinder.e` — выходной файл моделирования.
- `initial.csv` и `result.csv` — преобразованные координаты для анализа.

---

## Визуализация

1. Откройте `fragmenting_cylinder.e` в [ParaView](https://www.paraview.org/).
2. Нажмите **Apply** — отобразится начальное состояние.
3. Нажмите **Last Frame** — отобразится результат разрушения.

---

## Преобразование данных

Файл `preprocess.py` позволяет преобразовать результаты моделирования в удобный CSV-формат. На выходе получаются файлы:

- `initial.csv` — данные начального состояния.
- `result.csv` — данные конечного состояния.

Файл использует полярные координаты для приведения данных к цилиндрической форме. В коде указываются радиус и высота цилиндра.
