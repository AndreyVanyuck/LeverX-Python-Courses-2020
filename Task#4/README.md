# Оптимизация запросов
С помощью EXPLAIN будем анализировать количество записей, которые приходится прочитать базе данных для выполнения запроса.
| Название таблицы  | Кол-во записей в таблице |
| -------------     | ------------- |
| room              | 1000  |
| student           | 10000  |

![](https://sun2.beltelecom-by-minsk.userapi.com/impf/FIqL8GWF9ysrP6-1umrlilLJQKTg1TDQ9aXw4Q/x1EPg1NCbgw.jpg?size=408x440&quality=96&proxy=1&sign=3e310de7f566ae571805ce9a6811f50f)

## Запрос #1
![](https://sun9-62.userapi.com/impf/98a-Izzkt5L4vGOgxxrMAgefGs5O9D4cgHXvIg/49IExF3T9ps.jpg?size=1129x87&quality=96&proxy=1&sign=ce748aca0da709e99c43385dfa2e7584)
Как видим, не используется ни один индекс и было прочитано 1 * 9897 = 9897 записей.

```html
ALTER TABLE `python_student`.`student` 
ADD INDEX `room_ind` (`room` ASC) VISIBLE;
```
После создания индекса:
![](https://sun9-66.userapi.com/impf/IN_EPDmFwsrXBbCXovwzKD_zx7MBibRzYvoG1g/7rwhKU1a_UA.jpg?size=1061x73&quality=96&proxy=1&sign=ed20ba4e892d0fa4c0d1d5255c19ff8e)

Прочитано 9 * 1000 = 9000 , т.к. был использован индекс.
Как видим производительность выросла на ~10%. Для больших объёмов информации это будет уже существенно.

## Запрос #2
![](https://sun9-62.userapi.com/impf/98a-Izzkt5L4vGOgxxrMAgefGs5O9D4cgHXvIg/49IExF3T9ps.jpg?size=1129x87&quality=96&proxy=1&sign=ce748aca0da709e99c43385dfa2e7584)

После добавления индекса:
```html
ALTER TABLE `python_student`.`student` 
ADD INDEX `birthday_ind` (`room` ASC, `birthday` ASC) VISIBLE;
```
![](https://sun9-65.userapi.com/impf/A6HEVtxVjiywxSbxYB3KxpJGT0IEEBin_NO_3Q/ikNgSFgFK7Q.jpg?size=1204x72&quality=96&proxy=1&sign=ae7e59692564a668363a7fc243d3a670)

Видно, что оптимизатор БД выбрал наш созданный индекс. Кол-во прочитаных записей уменьшилось на ~10%.

## Запрос #3
Для запроса №3 оптимизатор БД использует уже созданый нами индекс для запроса №2. 
![](https://sun9-66.userapi.com/impf/CDyJlaVM2cmSh0BYxMASHs9zj9w5iI3PYDYT1w/wK7N8bpQJ2Y.jpg?size=1196x76&quality=96&proxy=1&sign=a399cdf3c993c39fee4cf69005f1b52d)

Создание других индексов не приводит к уменьшению кол-ва прочитаных записей.

## Запрос #4
![](https://sun9-41.userapi.com/impf/9aLz76vQbE_QUgWCld3h2nWvI2n0-ENeaQUltg/Kyy0YWgGQBA.jpg?size=1045x76&quality=96&proxy=1&sign=3b1feec2ec841f5d6f86af7d88a818d3)

Был выбран индекс, созданный в запросе №1. Но после добавления индекса:
```html
ALTER TABLE `python_student`.`student` 
ADD INDEX `sex_ind` (`room` ASC, `sex` ASC) VISIBLE;
```
![](https://sun9-2.userapi.com/impf/seIWVdnEtN26QeiTqxAe8DuvFHeU2t2eIxI0dg/VgWPUqHq7XQ.jpg?size=1115x72&quality=96&proxy=1&sign=07cb9cccbf0e77fcbc45a7cd3073f5c7)

Видим, что был выбран наш новый индекс. Хотя это не привело к росту производительности запроса.

# Заключение
Было предложено создать 3 индекса, которые сокращают кол-во прочитанных записей запросами на ~10%.
Получаем следующие таблицы:

![](https://sun1.beltelecom-by-minsk.userapi.com/impf/RHhhvX1ZYXO2rsSqQDxgn0XjPMUSS-UM1SrwCQ/KHLQwtRizhM.jpg?size=399x530&quality=96&proxy=1&sign=552e4f21885c5a67f68620c832b300cc)
