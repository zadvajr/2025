CREATE TABLE "User" (
  "user_id" INT PRIMARY KEY,
  "name" VARCHAR,
  "email" VARCHAR,
  "password" VARCHAR,
  "phone" VARCHAR,
  "address" TEXT,
  "created_at" TIMESTAMPTZ,
  "updated_at" TIMESTAMPTZ
);

CREATE TABLE "Product" (
  "product_id" INT PRIMARY KEY,
  "name" VARCHAR,
  "description" TEXT,
  "price" DECIMAL,
  "stock" INT,
  "category_id" INT,
  "created_at" TIMESTAMPTZ,
  "updated_at" TIMESTAMPTZ
);

CREATE TABLE "Category" (
  "category_id" INT PRIMARY KEY,
  "name" VARCHAR,
  "description" TEXT
);

CREATE TABLE "Order" (
  "order_id" INT PRIMARY KEY,
  "user_id" INT,
  "status" VARCHAR,
  "order_date" TIMESTAMPTZ,
  "total_price" DECIMAL,
  "created_at" TIMESTAMPTZ,
  "updated_at" TIMESTAMPTZ
);

CREATE TABLE "OrderItem" (
  "order_item_id" INT PRIMARY KEY,
  "order_id" INT,
  "product_id" INT,
  "quantity" INT,
  "price" DECIMAL
);

CREATE TABLE "Payment" (
  "payment_id" INT PRIMARY KEY,
  "order_id" INT,
  "amount" DECIMAL,
  "payment_method" VARCHAR,
  "payment_date" TIMESTAMPTZ,
  "status" VARCHAR
);

CREATE TABLE "Review" (
  "review_id" INT PRIMARY KEY,
  "user_id" INT,
  "product_id" INT,
  "rating" INT,
  "comment" TEXT,
  "review_date" TIMESTAMPTZ
);

ALTER TABLE "Product" ADD FOREIGN KEY ("category_id") REFERENCES "Category" ("category_id");

ALTER TABLE "Order" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("user_id");

ALTER TABLE "OrderItem" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("order_id");

ALTER TABLE "OrderItem" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("product_id");

ALTER TABLE "Payment" ADD FOREIGN KEY ("order_id") REFERENCES "Order" ("order_id");

ALTER TABLE "Review" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("user_id");

ALTER TABLE "Review" ADD FOREIGN KEY ("product_id") REFERENCES "Product" ("product_id");
