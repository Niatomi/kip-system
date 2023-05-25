print(
  "Start #################################################################"
);

db = db.getSiblingDB("kip_system_db");
db.createUser({
  user: "api",
  pwd: "api",
  roles: [{ role: "readWrite", db: "kip_system_db" }],
});
db.createCollection("device_description");

print("END #################################################################");
