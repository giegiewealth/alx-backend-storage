-- Creates an INDEX idx_name_first on the table that's called and a 1st letter of name.
CREATE INDEX idx_name_first ON names(name(1));
