import { ExcelFileName } from "@/types";
import { existsSync } from "fs";
import { excelFileLocation } from "./excel-file-location";

export const excelExists = (type: ExcelFileName): boolean => {
  const exists = existsSync(excelFileLocation(type));
  console.log("🚀 ~ excelExists ~ exists:", exists);
  return exists;
};
