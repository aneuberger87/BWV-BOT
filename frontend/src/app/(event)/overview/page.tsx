import InputUploadBox from "@/components/custom/input-upload-parent";
import { excelExists } from "@/lib/action-excel-exists";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Übersicht",
};

const Page = () => {
  return (
    <div className="flex flex-wrap items-stretch gap-6">
      <InputUploadBox
        label="Schülerliste hochladen"
        description="Laden Sie die Schülerliste hoch"
        validateFunction={() => excelExists("studentsList")}
        dataViewHref="/students"
        type="studentsList"
      />
      <InputUploadBox
        label="Firmenliste hochladen"
        description="Laden Sie die Firmenliste hoch"
        validateFunction={() => excelExists("companiesList")}
        dataViewHref="/companies"
        type="companiesList"
      />
      <InputUploadBox
        label="Raumliste hochladen"
        description="Laden Sie die Raumliste hoch"
        validateFunction={() => excelExists("roomsList")}
        dataViewHref="/rooms"
        type="roomsList"
      />
    </div>
  );
};

export default Page;

export const revalidate = 0;
export const dynamic = "force-dynamic";
