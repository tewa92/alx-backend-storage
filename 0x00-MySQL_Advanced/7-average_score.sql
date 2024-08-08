DROP PROCEDURE IF EXISTS ComputeAverageScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUsers()
BEGIN
UPDATE users
SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = users.id);
END $$
DELIMITER
