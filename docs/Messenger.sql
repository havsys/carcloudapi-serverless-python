CREATE TYPE "message_status" AS ENUM (
  'DRAFT',
  'QUEUE',
  'SENT',
  'FAIL'
);

CREATE TABLE "company" (
  "id" uuid PRIMARY KEY,
  "name" varchar NOT NULL,
  "currency" varchar NOT NULL,
  "send_cost" double NOT NULL,
  "send_cost_subsequent" double,
  "timezone" varchar NOT NULL,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

CREATE TABLE "company_credentials" (
  "company_id" uuid NOT NULL,
  "type" varchar NOT NULL,
  "login" varchar NOT NULL,
  "secret" varchar NOT NULL,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

CREATE TABLE "campaign" (
  "id" uuid PRIMARY KEY,
  "company_id" uuid,
  "template_id" uuid,
  "name" varchar NOT NULL,
  "type" varchar NOT NULL DEFAULT 'AUTOMATIC',
  "target_url" varchar NOT NULL,
  "schedule" varchar,
  "phone_field_name" varchar,
  "mobile_field_name" varchar,
  "billing_reference_field_name" varchar,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

CREATE TABLE "campaign_lang" (
  "campaign_id" uuid,
  "language" varchar(3) NOT NULL,
  "message_content" text NOT NULL,
  "sender_name" varchar(11) NOT NULL,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

CREATE TABLE "message_log" (
  "campaign_id" uuid,
  "company_id" uuid,
  "language" varchar(3) NOT NULL,
  "sender_name" varchar(11) NOT NULL,
  "content" text NOT NULL,
  "phone_number" varchar NOT NULL,
  "status" "message_status" NOT NULL DEFAULT 'DRAFT',
  "status_details" text,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime
);

CREATE TABLE "user" (
  "id" uuid PRIMARY KEY,
  "company_id" uuid NOT NULL,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

CREATE TABLE "template" (
  "id" uuid PRIMARY KEY,
  "name" varchar NOT NULL,
  "content" text NOT NULL,
  "created_at" datetime NOT NULL DEFAULT (now()),
  "updated_at" datetime,
  "deleted_at" datetime
);

ALTER TABLE "company_credentials" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

ALTER TABLE "campaign" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

ALTER TABLE "campaign" ADD FOREIGN KEY ("template_id") REFERENCES "template" ("id");

ALTER TABLE "campaign_lang" ADD FOREIGN KEY ("campaign_id") REFERENCES "campaign" ("id");

ALTER TABLE "message_log" ADD FOREIGN KEY ("campaign_id") REFERENCES "campaign" ("id");

ALTER TABLE "message_log" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");

ALTER TABLE "user" ADD FOREIGN KEY ("company_id") REFERENCES "company" ("id");
CREATE UNIQUE INDEX  
ON "company_credentials" ("company_id","type");

CREATE UNIQUE INDEX  
ON "campaign_lang" ("campaign_id","language");

CREATE UNIQUE INDEX  
ON "message_log" ("campaign_id","language");
