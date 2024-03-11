SELECT
    id,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree AS atree WHERE atree.p_id IS NULL)
            THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree AS atree)
            THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM
    tree
ORDER BY id


-- It is a pain to use UNION, while CASE WHEN is much better
-- Root's parent_id is NULL, and there should be only one such node in a tree
-- Inner should have its children, so its id should be included in all the p_id
-- Leaf doesn't have its children. If a node is neither inner nor root, it should be leaf.
