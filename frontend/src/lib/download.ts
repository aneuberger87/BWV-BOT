import { ExcelFileName } from "@/types";
import { existsSync } from "fs";
import { readFile } from "fs/promises";
import { excelFileLocation } from "./excel-file-location";
import {
  postPrintAttendanceList,
  postPrintRoomAssignmentList,
} from "./fetches";
import { getFrontendData, setFrontendData } from "./frontend-data";

export const downloadInputExcelAsBuffer = async (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  const exists = existsSync(path);
  if (exists) {
    const file = await readFile(path);
    return file;
  }
  return null;
};

const shareFolder = process.env.FOLDER_SHARE!;

const ATTENDENCE_LIST_FILE_NAME = "Anwesenheitsliste_pro_Veranstaltung.xlsx";
const ROOM_ASSIGNMENT_LIST_FILE_NAME = "Raum_und_Zeitplanung.xlsx";
const TIMETABLE_LIST_FILE_NAME = "UNKOWN"; //TODO
type CalcStatus = {
  calculated: boolean;
  downloaded: {
    students: boolean;
    rooms: boolean;
    companies: boolean;
  };
};

export const downloadOutputExcelAsBuffer = async (
  type: "attendenceList" | "rooAssignmentList" | "timetableList",
) => {
  let result = null;
  if (type === "rooAssignmentList") {
    result = await postPrintRoomAssignmentList(shareFolder);
  }
  if (type === "attendenceList") {
    result = await postPrintAttendanceList(shareFolder);
  }
  if (type === "timetableList") {
    result = await postPrintAttendanceList(shareFolder);
  }

  const fileName =
    type === "attendenceList"
      ? ATTENDENCE_LIST_FILE_NAME
      : type === "rooAssignmentList"
        ? ROOM_ASSIGNMENT_LIST_FILE_NAME
        : TIMETABLE_LIST_FILE_NAME;
  const filePath = `${shareFolder}${fileName}`;
  const exists = existsSync(filePath);
  if (exists) {
    const frontendData = getFrontendData();
    if (type === "rooAssignmentList") {
      frontendData.downloaded.rooms = true;
    }
    if (type === "attendenceList") {
      frontendData.downloaded.students = true;
    }
    if (type === "timetableList") {
      frontendData.downloaded.companies = true;
    }
    setFrontendData(frontendData);
    const file = await readFile(filePath);
    return file;
  }

  return null;
};
