"use server";

import { ExcelFileName } from "@/types";
import { excelFileLocation } from "./excel-file-location";
import { existsSync } from "fs";
import { readFile } from "fs/promises";

export const download = async (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  console.log("🚀 ~ download ~ path:", path);
  // get the content from the file if it exists and return it
  const exists = existsSync(path);
  if (exists) {
    const file = await readFile(path);
    console.log("🚀 ~ download ~ file:", file.toString());
    return {
      success: true,
      file: file.toString("base64"),
      error: null,
    };
  }
  return {
    success: false,
    file: null,
    error: "File does not exist",
  };
};

export const downloadAsBuffer = async (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  console.log("🚀 ~ download ~ path:", path);
  // get the content from the file if it exists and return it
  const exists = existsSync(path);
  if (exists) {
    const file = await readFile(path);
    return file;
  }
  return null;
};
