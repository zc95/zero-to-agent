-- 01 建表与查询
-- 在同一个数据库连接里按顺序执行。重新练习时，打开一个新的连接。

-- 1. 创建任务表，然后查一下空表。
-- id 由数据库生成，主键保证编号唯一。
-- title 必须有值，插入时省略 done 就用 false。
CREATE TEMP TABLE tasks (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title text NOT NULL,
    done boolean NOT NULL DEFAULT false
);

-- 预期看到 id、title、done 三列，结果有 0 行。
SELECT id, title, done FROM tasks;

-- 2. 加入一条待办任务和一条已完成任务。
INSERT INTO tasks (title) VALUES ('练习建表');
INSERT INTO tasks (title, done) VALUES ('复习 Python', true);

-- ORDER BY id 让结果按编号从小到大显示。
-- 预期结果
-- 1 | 练习建表    | false
-- 2 | 复习 Python | true
SELECT id, title, done
FROM tasks
ORDER BY id;

-- 3. 用 WHERE 保留未完成的任务，用 SELECT 只显示标题。
-- 预期只看到「练习建表」。
SELECT title
FROM tasks
WHERE done = false
ORDER BY id;

-- 4. 把筛选条件从 false 改成 true，再运行一次。
-- 预期只看到「复习 Python」。
SELECT title
FROM tasks
WHERE done = true
ORDER BY id;
