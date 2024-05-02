-- May 2, 2024
-- Status: Complete
-- Notes: Learned LENGTH() and CHAR_LENGTH() function. In this example, either works 
-- since these are ASCII characters but it would have different values if multi-byte characters

SELECT tweet_id 
FROM Tweets
WHERE LENGTH(content) > 15
