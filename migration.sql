create table user_property_junction
(
  user_id int,
  property_id int,
  relationship ENUM ('LIKE') DEFAULT 'LIKE',
  CONSTRAINT user_property_pk PRIMARY KEY (user_id, property_id),
  CONSTRAINT FK_user FOREIGN KEY (user_id) REFERENCES user (user_id),
  CONSTRAINT FK_property FOREIGN KEY (property_id) REFERENCES property_id (property_id)
);