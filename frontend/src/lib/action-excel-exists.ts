import { ExcelFileName } from "@/types";
import { existsSync } from "fs";
import { excelFileLocation } from "./excel-file-location";

export const excelExists = (type: ExcelFileName): boolean => {
  return existsSync(excelFileLocation(type));
};
