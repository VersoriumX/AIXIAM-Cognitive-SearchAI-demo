import { connectToDatabase } from "./utils/dbConnection";

const startApp = async () => {
  await connectToDatabase();
  console.log("Application is running...");
};

startApp();
