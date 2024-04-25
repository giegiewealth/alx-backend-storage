-- Creates an INDEX idx_name_first_score on the table that's called and
-- the 1st letter of name & the score.
CREATE INDEX idx_name_first_score ON names(name(1), score);
