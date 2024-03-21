import InputUploadBox from "@/components/custom/input-upload-parent";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { getDataStatusCachable } from "@/lib/data-status";
import { excelExists } from "@/lib/excel-exists";
import { Metadata } from "next";
import { FaRegCheckCircle } from "react-icons/fa";
import { FaDownload } from "react-icons/fa6";

export const metadata: Metadata = {
  title: "Übersicht",
};
const Download = (props: {
  title: string;
  type: "attendence-list" | "room-assignment-list" | "timetable-list";
}) => {
  const url = `/api/calculated/${props.type}`;
  return (
    <Button variant="secondary" className="flex-grow" asChild>
      <a href={url} download={`${props.type}.xlsx`}>
        <FaDownload className="mr-4" />
        {props.title}
      </a>
    </Button>
  );
};
const WhenCalculated = () => {
  return (
    <Card className="flex h-full flex-col justify-between">
      <CardHeader>
        <CardTitle className="flex items-center justify-start gap-4">
          <FaRegCheckCircle className="text-green-500" />
          Eine Auslosung liegt bereits vor
        </CardTitle>
        <CardDescription>
          Sie können die Auslosung herunterladen, um die Ergebnisse zu nutzen.
        </CardDescription>
      </CardHeader>
      <CardContent className="h-full">
        <div className="m-auto grid w-max grid-cols-3 justify-center gap-2">
          <Download title="Anwesenheits Excel" type="attendence-list" />
          <Download title="Raumaufteilungs Excel" type="room-assignment-list" />
          <Download title="Zeiten Excel" type="timetable-list" />
        </div>
      </CardContent>
      <CardFooter></CardFooter>
    </Card>
  );
};

const Page = () => {
  const data = getDataStatusCachable();
  const isCalculated = data.output.calculated;

  return (
    <>
      {isCalculated ? (
        WhenCalculated()
      ) : (
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
      )}
    </>
  );
};

export default Page;

export const revalidate = 0;
export const dynamic = "force-dynamic";
