create table user_property_junction
(
  auth_user_id int,
  property_id int,
  relationship ENUM ('LIKE') DEFAULT 'LIKE',
  CONSTRAINT user_property_pk PRIMARY KEY (auth_user_id, property_id),
  CONSTRAINT FK_user FOREIGN KEY (auth_user_id) REFERENCES user (auth_user_id),
  CONSTRAINT FK_property FOREIGN KEY (property_id) REFERENCES property_id (property_id)
);