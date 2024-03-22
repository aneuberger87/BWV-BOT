import InputUploadBox from "@/components/custom/input-upload-parent";
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
import { getSolutionScore } from "@/lib/fetches";
import { Metadata } from "next";
import { FaRegCheckCircle, FaTimes } from "react-icons/fa";
import { ClickAll } from "./click-all";
import { Download } from "./donwload-button";

export const metadata: Metadata = {
  title: "Übersicht",
};

const WhenCalculated = async () => {
  const score = await getSolutionScore();
  return (
    <Card className="flex h-full flex-col justify-between">
      <CardHeader className="pb-0">
        <CardTitle className="flex items-center justify-start gap-4">
          <FaRegCheckCircle className="text-green-500" />
          Eine Auslosung liegt bereits vor
        </CardTitle>
        <CardDescription className="pt-2">
          Hier finden Sie die Ergebnisse der Auslosung. <br />
          Der Score gibt, ausgehend von den schulischen Vorgaben, an, wie gut
          die Aufteilung ist. <br />
          Die Schüler- und Firmendaten können Sie oben im Menü einsehen. <br />
          Dort können auch die Raumzuteilungen angepasst werden. <br />
        </CardDescription>
      </CardHeader>
      <CardContent className="h-full pt-0">
        <div className="my-6 mt-10 grid grid-cols-[1fr_auto_1fr] items-center gap-2">
          <Separator />
          <div className="text-2xl font-bold">Score</div>
          <Separator />
        </div>
        <div className="mt-2 flex items-center gap-2 text-3xl font-bold">
          {score.realScore > 0 ? (
            <div className="m-auto">
              <span>{Math.floor(score.realScore * 100)}</span>
              <span className="text-xl">
                .{(score.realScore * 100).toFixed(2).split(".")[1]}
              </span>
              <span>%</span>
            </div>
          ) : (
            <FaTimes className="relative top-0.5 m-auto text-red-500" />
          )}
        </div>
        {score.errorMessage && (
          <div className="m-auto text-sm text-red-500">
            {score.errorMessage}
          </div>
        )}
        <div className="my-6 mt-12 grid grid-cols-[1fr_auto_1fr] items-center gap-2">
          <Separator />
          <div className="text-2xl font-bold">Downloads</div>
          <Separator />
        </div>
        <div className="m-auto w-max">
          <ClickAll
            idsToClick={[
              "attendence-list",
              "room-assignment-list",
              "timetable-list",
            ]}
          />
        </div>
        <div className="m-auto mt-2 grid w-max grid-cols-3 justify-center gap-2">
          <Download
            title="Anwesenheitslisten"
            type="attendence-list"
            id="attendence-list"
          />
          <Download
            title="Raumaufteilungsliste"
            type="room-assignment-list"
            id="room-assignment-list"
          />
          <Download
            title="Laufzettel"
            type="timetable-list"
            id="timetable-list"
          />
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
