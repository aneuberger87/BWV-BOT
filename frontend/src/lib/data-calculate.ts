"use server";
import { webhookCalculate } from "./fetches";
import { existsSync, writeFileSync } from "fs";
import { setFrontendData } from "./frontend-data";

export const dataCalculate = async () => {
  // TODO remove this timeout
  await new Promise((resolve) => setTimeout(resolve, 2000));

  const result = await webhookCalculate().catch((e) =>
    console.error("Error in dataCalculate", e),
  );
  setFrontendData({
    calculated: true,
    downloaded: {
      students: false,
      rooms: false,
      companies: false,
    },
  });
  console.log("🚀 ~ dataCalculate ~ result:", result);
  return result;
};
