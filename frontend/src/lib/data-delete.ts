"use server";

import { ExcelFileName } from "@/types";
import { existsSync, unlinkSync } from "fs";
import { excelFileLocation } from "./excel-file-location";
const URL = process.env.DATAMANAGEMENT_URL!;

export const dataDelete = async (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  if (existsSync(path)) {
    unlinkSync(path);
  }
  const response = await fetch(URL + type + "?fileLocation=" + "EMPTY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: "",
  });
  return { success: true };
};
