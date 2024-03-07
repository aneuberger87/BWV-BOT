"use server";

import { ExcelFileName } from "@/types";
import { excelFileLocation } from "./excel-file-location";
import { existsSync, unlinkSync } from "fs";

export const deleteData = (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  if (existsSync(path)) {
    unlinkSync(path);
  }
  return { success: true };
};
