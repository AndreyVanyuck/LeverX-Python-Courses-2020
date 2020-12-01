select_number_of_students_in_room = """
SELECT room.name, COUNT(*) AS count_students
FROM room
INNER JOIN student ON room.id = student.room
GROUP BY room.id
"""


select_top_five_small_avg_age_rooms = """
SELECT room.name, CAST(AVG(YEAR(CURRENT_DATE) - YEAR(birthday)) as double)  as avg_age 
FROM room 
INNER JOIN student ON room.id = student.room
GROUP BY room.id
ORDER BY avg_age
LIMIT 5
"""


select_top_five_big_diff_age_rooms = """
SELECT room.name, MAX(YEAR(birthday)) - MIN(YEAR(birthday)) as diff
FROM room
INNER JOIN student ON room.id = student.room
GROUP BY room.id
ORDER BY diff DESC
LIMIT 5
"""


select_different_sexes_rooms = """
SELECT room.name, room.id
FROM room
INNER JOIN student ON room.id = student.room
GROUP BY room.id
HAVING SUM(CASE WHEN sex = 'M' THEN 1 ELSE 0 END) > 0 and SUM(CASE WHEN sex = 'F' THEN 1 ELSE 0 END) > 0
ORDER BY room.id
"""

insert_into_room = """
INSERT INTO room ( id, name ) 
VALUES (  %s, %s )
"""


insert_into_student = """
INSERT INTO student ( birthday, id, name, room, sex ) 
VALUES ( %s, %s, %s, %s, %s )
"""


create_index_room = """
ALTER TABLE `python_student`.`student` 
ADD INDEX `room_ind` (`room` ASC) VISIBLE;
"""

create_index_birthday = """
ALTER TABLE `python_student`.`student` 
ADD INDEX `birthday_ind` (`room` ASC, `birthday` ASC) VISIBLE;
"""
create_index_sex = """
ALTER TABLE `python_student`.`student` 
ADD INDEX `sex_ind` (`room` ASC, `sex` ASC) VISIBLE;
"""
