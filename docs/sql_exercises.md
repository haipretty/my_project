**SQL数据库专项练习题（含参考答案）**

**前言**

本文档匹配计划学习SQL的朋友，涵盖**基础查询、聚合分组、多表连接、子查询、数据操作、表结构设计、综合项目**全知识点。所有题目均提供了可直接执行的初始化SQL和最优参考答案，建议先独立完成题目，再核对答案。

**一、核心知识点覆盖**

1.  基础查询（SELECT/WHERE/ORDER BY/LIMIT/DISTINCT）

<!-- -->

2.  聚合函数（COUNT/SUM/AVG/MAX/MIN）+ GROUP BY + HAVING

<!-- -->

3.  多表连接（INNER JOIN/LEFT JOIN/RIGHT JOIN）

<!-- -->

4.  子查询（嵌套查询、关联子查询、EXISTS）

<!-- -->

5.  数据操作（INSERT/UPDATE/DELETE）

<!-- -->

6.  表结构设计（CREATE TABLE/ALTER TABLE/约束：主键/外键/唯一/非空）

<!-- -->

7.  条件逻辑（CASE WHEN）

<!-- -->

8.  窗口函数（RANK()/ROW_NUMBER()）

<!-- -->

9.  日期函数与集合运算

**二、基础练习题（共15题）**

**场景1：学生成绩管理系统**

**初始化SQL（先执行）**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SQL<br />
-- 1. 创建学生表<br />
CREATE TABLE students (<br />
student_id INT PRIMARY KEY AUTO_INCREMENT,<br />
student_name VARCHAR(50) NOT NULL,<br />
gender CHAR(2) CHECK (gender IN ('男', '女')),<br />
age INT,<br />
class VARCHAR(20)<br />
);<br />
<br />
-- 2. 创建课程表<br />
CREATE TABLE courses (<br />
course_id INT PRIMARY KEY AUTO_INCREMENT,<br />
course_name VARCHAR(50) NOT NULL UNIQUE,<br />
teacher_name VARCHAR(50) NOT NULL<br />
);<br />
<br />
-- 3. 创建成绩表<br />
CREATE TABLE scores (<br />
score_id INT PRIMARY KEY AUTO_INCREMENT,<br />
student_id INT NOT NULL,<br />
course_id INT NOT NULL,<br />
score INT CHECK (score BETWEEN 0 AND 100),<br />
exam_date DATE,<br />
FOREIGN KEY (student_id) REFERENCES students(student_id),<br />
FOREIGN KEY (course_id) REFERENCES courses(course_id),<br />
UNIQUE (student_id, course_id)<br />
);<br />
<br />
-- 插入测试数据<br />
INSERT INTO students (student_name, gender, age, class)<br />
VALUES<br />
('张三', '男', 16, '高一(1)班'),<br />
('李四', '女', 16, '高一(1)班'),<br />
('王五', '男', 17, '高一(2)班'),<br />
('赵六', '女', 16, '高一(2)班'),<br />
('钱七', '男', 17, '高一(1)班');<br />
<br />
INSERT INTO courses (course_name, teacher_name)<br />
VALUES<br />
('数学', '王老师'),<br />
('语文', '李老师'),<br />
('英语', '张老师'),<br />
('物理', '刘老师');<br />
<br />
INSERT INTO scores (student_id, course_id, score, exam_date)<br />
VALUES<br />
(1, 1, 85, '2026-01-10'),<br />
(1, 2, 92, '2026-01-11'),<br />
(2, 1, 95, '2026-01-10'),<br />
(2, 3, 88, '2026-01-12'),<br />
(3, 2, 78, '2026-01-11'),<br />
(3, 4, 90, '2026-01-13'),<br />
(4, 1, 65, '2026-01-10'),<br />
(4, 3, 72, '2026-01-12'),<br />
(5, 2, 80, '2026-01-11'),<br />
(5, 4, 89, '2026-01-13');</td>
</tr>
</tbody>
</table>

**题目1-8**

|      |            |                                                                           |
|------|------------|---------------------------------------------------------------------------|
| 题号 | 题目类型   | 需求描述                                                                  |
| 1    | 基础查询   | 查询「高一(1)班」所有女生的姓名、年龄，按年龄降序排列                     |
| 2    | 去重与限制 | 查询所有有成绩的班级（不重复），并只显示前1个班级                         |
| 3    | 聚合函数   | 计算「数学」课程的平均分，以及参加数学考试的学生人数                      |
| 4    | 分组查询   | 按班级分组，统计每个班级的学生人数，只显示人数≥3的班级                    |
| 5    | 条件逻辑   | 查询所有学生的姓名、数学成绩，并按成绩分级（≥90=A，≥80=B，≥60=C，\<60=D） |
| 6    | 子查询     | 查询「语文」成绩高于班级平均分的学生姓名、班级、语文成绩                  |
| 7    | 数据更新   | 将「赵六」的英语成绩提高5分（英语课程ID=3，赵六学生ID=4）                 |
| 8    | 数据删除   | 删除「高一(2)班」年龄大于17岁的学生（先处理外键约束）                     |

**参考答案1-8**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SQL<br />
-- 题1<br />
SELECT student_name, age<br />
FROM students<br />
WHERE class = '高一(1)班' AND gender = '女'<br />
ORDER BY age DESC;<br />
<br />
-- 题2<br />
SELECT DISTINCT s.class<br />
FROM students s<br />
JOIN scores sc ON s.student_id = sc.student_id<br />
LIMIT 1;<br />
<br />
-- 题3<br />
SELECT<br />
AVG(sc.score) AS 数学平均分,<br />
COUNT(sc.student_id) AS 参考人数<br />
FROM courses c<br />
JOIN scores sc ON c.course_id = sc.course_id<br />
WHERE c.course_name = '数学';<br />
<br />
-- 题4<br />
SELECT class, COUNT(student_id) AS 学生人数<br />
FROM students<br />
GROUP BY class<br />
HAVING COUNT(student_id) &gt;= 3;<br />
<br />
-- 题5<br />
SELECT<br />
s.student_name,<br />
sc.score AS 数学成绩,<br />
CASE<br />
WHEN sc.score &gt;= 90 THEN 'A'<br />
WHEN sc.score &gt;= 80 THEN 'B'<br />
WHEN sc.score &gt;= 60 THEN 'C'<br />
ELSE 'D'<br />
END AS 成绩等级<br />
FROM students s<br />
LEFT JOIN scores sc ON s.student_id = sc.student_id<br />
LEFT JOIN courses c ON sc.course_id = c.course_id AND c.course_name =
'数学';<br />
<br />
-- 题6<br />
SELECT<br />
s.student_name,<br />
s.class,<br />
sc.score AS 语文成绩<br />
FROM students s<br />
JOIN scores sc ON s.student_id = sc.student_id<br />
JOIN courses c ON sc.course_id = c.course_id AND c.course_name =
'语文'<br />
WHERE sc.score &gt; (<br />
SELECT AVG(sc2.score)<br />
FROM scores sc2<br />
JOIN students s2 ON sc2.student_id = s2.student_id<br />
JOIN courses c2 ON sc2.course_id = c2.course_id<br />
WHERE c2.course_name = '语文' AND s2.class = s.class<br />
);<br />
<br />
-- 题7<br />
UPDATE scores<br />
SET score = score + 5<br />
WHERE student_id = 4 AND course_id = 3;<br />
<br />
-- 题8<br />
-- 第一步：先删除该学生的成绩记录<br />
DELETE FROM scores<br />
WHERE student_id IN (<br />
SELECT student_id FROM students WHERE class = '高一(2)班' AND age &gt;
17<br />
);<br />
-- 第二步：删除学生记录<br />
DELETE FROM students<br />
WHERE class = '高一(2)班' AND age &gt; 17;</td>
</tr>
</tbody>
</table>

**场景2：商品销售系统**

**初始化SQL（先执行）**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SQL<br />
-- 1. 商品表<br />
CREATE TABLE products (<br />
product_id INT PRIMARY KEY AUTO_INCREMENT,<br />
product_name VARCHAR(50) NOT NULL,<br />
category VARCHAR(30),<br />
price DECIMAL(10,2) NOT NULL,<br />
stock INT NOT NULL DEFAULT 0<br />
);<br />
<br />
-- 2. 订单表<br />
CREATE TABLE orders (<br />
order_id INT PRIMARY KEY AUTO_INCREMENT,<br />
user_id INT NOT NULL,<br />
order_date DATETIME NOT NULL,<br />
total_amount DECIMAL(10,2)<br />
);<br />
<br />
-- 3. 订单详情表<br />
CREATE TABLE order_details (<br />
detail_id INT PRIMARY KEY AUTO_INCREMENT,<br />
order_id INT NOT NULL,<br />
product_id INT NOT NULL,<br />
quantity INT NOT NULL,<br />
unit_price DECIMAL(10,2) NOT NULL,<br />
FOREIGN KEY (order_id) REFERENCES orders(order_id),<br />
FOREIGN KEY (product_id) REFERENCES products(product_id)<br />
);<br />
<br />
-- 插入测试数据<br />
INSERT INTO products (product_name, category, price, stock)<br />
VALUES<br />
('手机', '电子产品', 3999.00, 50),<br />
('笔记本电脑', '电子产品', 5999.00, 30),<br />
('T恤', '服装', 99.00, 200),<br />
('牛仔裤', '服装', 199.00, 150),<br />
('耳机', '电子产品', 299.00, 100);<br />
<br />
INSERT INTO orders (user_id, order_date, total_amount)<br />
VALUES<br />
(101, '2026-02-01 10:30:00', 4298.00),<br />
(102, '2026-02-02 14:15:00', 6198.00),<br />
(101, '2026-02-03 09:45:00', 298.00),<br />
(103, '2026-02-04 16:20:00', 5999.00),<br />
(102, '2026-02-05 11:50:00', 499.00);<br />
<br />
INSERT INTO order_details (order_id, product_id, quantity,
unit_price)<br />
VALUES<br />
(1, 1, 1, 3999.00),<br />
(1, 5, 1, 299.00),<br />
(2, 2, 1, 5999.00),<br />
(2, 3, 1, 99.00),<br />
(3, 3, 2, 99.00),<br />
(4, 2, 1, 5999.00),<br />
(5, 5, 1, 299.00),<br />
(5, 4, 1, 199.00);</td>
</tr>
</tbody>
</table>

**题目9-15**

|      |              |                                                                                       |
|------|--------------|---------------------------------------------------------------------------------------|
| 题号 | 题目类型     | 需求描述                                                                              |
| 9    | 内连接       | 查询所有订单的「订单ID、下单时间、商品名称、购买数量」，只显示有商品的订单            |
| 10   | 左连接       | 查询所有商品的「商品名称、分类、销售总量」，无销售的显示为0                           |
| 11   | 复杂分组     | 按「商品分类、用户ID」分组，统计每个用户在每个分类下的购买总金额、总数量              |
| 12   | 日期筛选     | 查询2026年2月2日-2月4日的所有订单，显示订单ID、用户ID、总金额、下单日期（仅年月日）   |
| 13   | 表结构修改   | 给商品表添加字段「brand VARCHAR(30)」，并将所有电子产品的brand设为「华为」            |
| 14   | 删除表与约束 | 删除订单详情表关联orders表的外键约束，然后删除订单表                                  |
| 15   | 综合查询     | 查询购买过2个及以上不同分类商品的用户ID，以及他们的订单总数、消费总金额，按总金额降序 |

**参考答案9-15**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SQL<br />
-- 题9<br />
SELECT<br />
o.order_id,<br />
o.order_date,<br />
p.product_name,<br />
od.quantity<br />
FROM orders o<br />
JOIN order_details od ON o.order_id = od.order_id<br />
JOIN products p ON od.product_id = p.product_id;<br />
<br />
-- 题10<br />
SELECT<br />
p.product_name,<br />
p.category,<br />
IFNULL(SUM(od.quantity), 0) AS 销售总量<br />
FROM products p<br />
LEFT JOIN order_details od ON p.product_id = od.product_id<br />
GROUP BY p.product_id, p.product_name, p.category;<br />
<br />
-- 题11<br />
SELECT<br />
p.category,<br />
o.user_id,<br />
SUM(od.quantity) AS 购买总数量,<br />
SUM(od.quantity * od.unit_price) AS 购买总金额<br />
FROM orders o<br />
JOIN order_details od ON o.order_id = od.order_id<br />
JOIN products p ON od.product_id = p.product_id<br />
GROUP BY p.category, o.user_id;<br />
<br />
-- 题12<br />
SELECT<br />
order_id,<br />
user_id,<br />
total_amount,<br />
DATE(order_date) AS 下单日期<br />
FROM orders<br />
WHERE order_date BETWEEN '2026-02-02' AND '2026-02-04 23:59:59';<br />
<br />
-- 题13<br />
-- 添加字段<br />
ALTER TABLE products ADD COLUMN brand VARCHAR(30);<br />
-- 批量赋值<br />
UPDATE products<br />
SET brand = '华为'<br />
WHERE category = '电子产品';<br />
<br />
-- 题14<br />
-- 第一步：查询外键约束名（替换为你的实际约束名）<br />
-- SHOW CREATE TABLE order_details;<br />
-- 第二步：删除外键约束<br />
ALTER TABLE order_details DROP FOREIGN KEY order_details_ibfk_1;<br />
-- 第三步：删除订单表<br />
DROP TABLE orders;<br />
<br />
-- 题15<br />
SELECT<br />
o.user_id,<br />
COUNT(DISTINCT o.order_id) AS 订单总数,<br />
SUM(od.quantity * od.unit_price) AS 消费总金额<br />
FROM orders o<br />
JOIN order_details od ON o.order_id = od.order_id<br />
JOIN products p ON od.product_id = p.product_id<br />
GROUP BY o.user_id<br />
HAVING COUNT(DISTINCT p.category) &gt;= 2<br />
ORDER BY 消费总金额 DESC;</td>
</tr>
</tbody>
</table>

**三、高频难点进阶练习题（共5题·多表连接+子查询）**

基于上述两个场景的现有数据，无需重新建表。

**题目**

|       |                                                                                              |                                          |
|-------|----------------------------------------------------------------------------------------------|------------------------------------------|
| 题号  | 需求描述                                                                                     | 考察知识点                               |
| 进阶1 | 查询每个班级的班级名称、总人数、数学平均分、语文平均分、物理平均分，按数学平均分降序         | 多表左连接、条件聚合、排序               |
| 进阶2 | 查询所有课程都有成绩的学生姓名、班级，以及他们的总成绩和平均成绩                             | NOT EXISTS关联子查询、多表关联、聚合     |
| 进阶3 | 查询每个班级数学成绩排名前2的学生姓名、班级、数学成绩，并列排名全部显示                      | 窗口函数RANK()、子查询、分组排名         |
| 进阶4 | 查询购买过所有电子产品分类商品的用户ID，以及他们的订单总数、消费总金额、平均客单价           | 子查询统计分类数量、HAVING筛选、聚合组合 |
| 进阶5 | 查询既购买过手机又购买过笔记本电脑的用户ID，以及他们的首次下单时间、最后下单时间、总消费金额 | IN子查询、MIN/MAX日期函数、聚合          |

**参考答案**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SQL<br />
-- 进阶1<br />
SELECT<br />
s.class,<br />
COUNT(DISTINCT s.student_id) AS 总人数,<br />
AVG(CASE WHEN c.course_name = '数学' THEN sc.score END) AS
数学平均分,<br />
AVG(CASE WHEN c.course_name = '语文' THEN sc.score END) AS
语文平均分,<br />
AVG(CASE WHEN c.course_name = '物理' THEN sc.score END) AS
物理平均分<br />
FROM students s<br />
LEFT JOIN scores sc ON s.student_id = sc.student_id<br />
LEFT JOIN courses c ON sc.course_id = c.course_id<br />
GROUP BY s.class<br />
ORDER BY 数学平均分 DESC;<br />
<br />
-- 进阶2<br />
SELECT<br />
s.student_name,<br />
s.class,<br />
SUM(sc.score) AS 总成绩,<br />
AVG(sc.score) AS 平均成绩<br />
FROM students s<br />
JOIN scores sc ON s.student_id = sc.student_id<br />
WHERE NOT EXISTS (<br />
SELECT c.course_id<br />
FROM courses c<br />
WHERE NOT EXISTS (<br />
SELECT sc2.score_id<br />
FROM scores sc2<br />
WHERE sc2.student_id = s.student_id AND sc2.course_id =
c.course_id<br />
)<br />
)<br />
GROUP BY s.student_id, s.student_name, s.class;<br />
<br />
-- 进阶3<br />
SELECT student_name, class, 数学成绩<br />
FROM (<br />
SELECT<br />
s.student_name,<br />
s.class,<br />
sc.score AS 数学成绩,<br />
RANK() OVER (PARTITION BY s.class ORDER BY sc.score DESC) AS 排名<br />
FROM students s<br />
JOIN scores sc ON s.student_id = sc.student_id<br />
JOIN courses c ON sc.course_id = c.course_id AND c.course_name =
'数学'<br />
) AS t<br />
WHERE 排名 &lt;= 2;<br />
<br />
-- 进阶4<br />
SELECT<br />
o.user_id,<br />
COUNT(DISTINCT o.order_id) AS 订单总数,<br />
SUM(od.quantity * od.unit_price) AS 消费总金额,<br />
SUM(od.quantity * od.unit_price) / COUNT(DISTINCT o.order_id) AS
平均客单价<br />
FROM orders o<br />
JOIN order_details od ON o.order_id = od.order_id<br />
JOIN products p ON od.product_id = p.product_id<br />
WHERE p.category = '电子产品'<br />
GROUP BY o.user_id<br />
HAVING COUNT(DISTINCT p.product_id) = (<br />
SELECT COUNT(product_id) FROM products WHERE category = '电子产品'<br />
);<br />
<br />
-- 进阶5<br />
SELECT<br />
o.user_id,<br />
MIN(o.order_date) AS 首次下单时间,<br />
MAX(o.order_date) AS 最后下单时间,<br />
SUM(od.quantity * od.unit_price) AS 总消费金额<br />
FROM orders o<br />
JOIN order_details od ON o.order_id = od.order_id<br />
JOIN products p ON od.product_id = p.product_id<br />
WHERE o.user_id IN (<br />
SELECT o2.user_id<br />
FROM orders o2<br />
JOIN order_details od2 ON o2.order_id = od2.order_id<br />
JOIN products p2 ON od2.product_id = p2.product_id<br />
WHERE p2.product_name = '手机'<br />
) AND o.user_id IN (<br />
SELECT o3.user_id<br />
FROM orders o3<br />
JOIN order_details od3 ON o3.order_id = od3.order_id<br />
JOIN products p3 ON od3.product_id = p3.product_id<br />
WHERE p3.product_name = '笔记本电脑'<br />
)<br />
GROUP BY o.user_id;</td>
</tr>
</tbody>
</table>
