drop database if exists bep;
CREATE DATABASE bep;
use bep;

CREATE TABLE post (
    postID varchar(255) NOT NULL PRIMARY KEY,
    subreddit varchar(255) NOT NULL,
    time datetime NOT NULL,
    emotion varchar(255) NOT NULL,
    aggregate_emotion varchar(255) NULL,
    importance decimal(30,15) NOT NULL,
    importance_scaled decimal(30,15) NOT NULL,
    continent varchar(255) NOT NULL,
    topic varchar(255) NULL
)
