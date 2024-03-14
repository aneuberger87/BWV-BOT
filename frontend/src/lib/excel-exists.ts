import { ExcelFileName } from "@/types";
import { existsSync } from "fs";
import { excelFileLocation } from "./excel-file-location";
import { cache } from "react";

export const excelExists = cache((type: ExcelFileName): boolean => {
  return existsSync(excelFileLocation(type));
});
