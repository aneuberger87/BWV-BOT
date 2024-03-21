"use client";
import React from "react";
import { Button } from "../ui/button";
import { FaFileDownload } from "react-icons/fa";
import { ExcelFileName } from "@/types";
import { excelFileName } from "@/lib/excel-file-name";

const ButtonDownloadExcel = (props: { type: ExcelFileName }) => {
  const url =
    props.type === "companiesList"
      ? "/api/download-companies"
      : props.type === "studentsList"
        ? "/api/download-students"
        : "/api/download-rooms";

  return (
    <Button size="icon" variant="outline" type="button" asChild>
      <a href={url} download={excelFileName(props.type)}>
        <FaFileDownload />
      </a>
    </Button> // Button element to trigger download
  );
};

export default ButtonDownloadExcel;
