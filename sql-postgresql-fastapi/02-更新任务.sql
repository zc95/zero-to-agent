-- 02 更新任务
-- 先运行 01-建表与查询.sql，再在同一个数据库连接里执行本文件。

-- 1. SET 指定新值，WHERE 将更新范围限定为编号 1。
-- 预期更新 1 行。省略 WHERE 会更新表里的所有任务。
UPDATE tasks
SET done = true
WHERE id = 1;

-- 2. 查一下所有任务。预期仍有两条任务，done 都是 true。
SELECT id, title, done
FROM tasks
ORDER BY id;

-- 3. 再查待办任务。预期结果有 0 行。
SELECT title
FROM tasks
WHERE done = false;
