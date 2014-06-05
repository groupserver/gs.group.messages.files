SET CLIENT_ENCODING = 'UTF8';
SET CLIENT_MIN_MESSAGES = WARNING;

-- The file metadata, or the attachments, if you prefer.
CREATE TABLE file (
    file_id    TEXT                      NOT NULL,
    mime_type  TEXT                      NOT NULL 
                                         DEFAULT 'application/octet-stream'::TEXT,
    file_name  TEXT                      NOT NULL,
    -- File size in bytes
    file_size  INTEGER                   NOT NULL,
    date       TIMESTAMP WITH TIME ZONE  NOT NULL DEFAULT NOW(),
    post_id    TEXT                      NOT NULL REFERENCES post(post_id),
    topic_id   TEXT                      NOT NULL REFERENCES topic(topic_id)
);
