import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import ListTask from "./list-task";
import { PageStudent } from "./students/page-student";
import { PageCompany } from "./firmen/page-company";
import { ScrollArea } from "@/components/ui/scroll-area";

const EventLayout = (props: { children: React.ReactNode }) => {
  return (
    <div className="grid grid-cols-[auto_1fr] h-full gap-x-8 ">
      <div className="">
        <Card className="max-h-full min-h-full h-0 grid grid-rows-[auto_1fr] min-w-96">
          <CardHeader>
            <CardTitle>Event Details</CardTitle>
            <CardDescription className="w-min min-w-full">
              In dieser Liste sind alle Schritte aufgelistet, die für das Event
              erledigt werden müssen.
            </CardDescription>
          </CardHeader>
          <CardContent className="h-full">
            <div className="flex flex-col h-full justify-between">
              <div>
                <ListTask />
              </div>
              <div className="flex flex-col gap-4">
                <Button disabled>Auslosen</Button>
                <div className="flex gap-4">
                  <Button disabled className="grow">
                    Ergebnis
                  </Button>
                  <Button disabled>Drucken</Button>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
      <div className="flex flex-col gap-4 max-h-full min-h-full h-0">
        <Tabs defaultValue="overview" className="min-h-full flex flex-col">
          <TabsList className="grid  grid-cols-5 gap-x-4 mb-6">
            <TabsTrigger value="overview" className="col-span-2">
              Überischt
            </TabsTrigger>
            <TabsTrigger value="students">Schülerliste</TabsTrigger>
            <TabsTrigger value="companies">Firmenliste</TabsTrigger>
            <TabsTrigger value="rooms">Raumliste</TabsTrigger>
          </TabsList>
          <TabsContent value="overview">{props.children}</TabsContent>
          <TabsContent value="students" className="grow">
            <PageStudent />
          </TabsContent>
          <TabsContent value="companies" className="grow flex flex-col">
            <PageCompany />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};

export default EventLayout;

export const revalidate = 0;
export const dynamic = "force-dynamic";
