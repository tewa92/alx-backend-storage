-- creates an index idx_name_first_score on the table names for
-- the columns name and score
CREATE INDEX idx_name_first_score ON names(name(1), score);