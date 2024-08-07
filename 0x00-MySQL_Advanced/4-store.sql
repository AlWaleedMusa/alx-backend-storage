-- This SQL script creates a trigger named 'DECREMENT' that is executed after a new row is inserted into the 'orders' table.
-- The purpose of the trigger is to decrement the quantity of an item in the 'items' table based on the number of items ordered.

CREATE TRIGGER DECREMENT
AFTER INSERT  -- The trigger is executed after a new row is inserted into the 'orders' table
ON orders  -- The trigger is associated with the 'orders' table
FOR EACH ROW  -- The trigger is executed for each row that is inserted
UPDATE items  -- Update the 'items' table
SET quantity = quantity - NEW.number  -- Decrement the quantity of the item by the number of items ordered
WHERE NAME = NEW.item_name;  -- The item to update is identified by matching the 'name' column in the 'items' table with the 'item_name' column in the new row of the 'orders' table
