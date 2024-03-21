import { existsSync, readFileSync, writeFileSync } from "fs";

const SHARE_FOLDER = process.env.FOLDER_SHARE!;
const STATUS_FILE_NAME = "frontend-data.json";

type frontendData = {
  calculated: boolean;
  downloaded: {
    students: boolean;
    rooms: boolean;
    companies: boolean;
  };
};

export const getFrontendData = () => {
  if (existsSync(SHARE_FOLDER + STATUS_FILE_NAME) === false) {
    return {
      calculated: false,
      downloaded: {
        students: false,
        rooms: false,
        companies: false,
      },
    };
  }
  const fileContent = readFileSync(SHARE_FOLDER + STATUS_FILE_NAME, "utf-8");
  const status: frontendData = JSON.parse(fileContent);
  return status;
};

export const setFrontendData = (status: frontendData) => {
  const fileContent = JSON.stringify(status, null, 2);
  const filePath = `${SHARE_FOLDER}${STATUS_FILE_NAME}`;
  writeFileSync(filePath, fileContent);
};
