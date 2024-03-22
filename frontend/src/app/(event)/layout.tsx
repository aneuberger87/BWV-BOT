import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import ListTask from "./list-task";
import { MainMenu } from "./menu";
import { Metadata } from "next";
import { ButtonPrint } from "@/components/custom/button-print";
import { ButtonCalculate } from "@/components/custom/button-calculate";
import { getDataStatusCachable } from "@/lib/data-status";
import { ButtonCalculateReset } from "@/components/custom/button-calculate-Reset";
import { HelpWrapper } from "@/components/custom/help-wrapper";

export const metadata: Metadata = {
  title: {
    default: "BWV BOT",
    template: "%s | BWV BOT",
  },
};

const EventLayout = (props: { children: React.ReactNode }) => {
  const dataExists = getDataStatusCachable().input.excel.allExist;
  const calculationExists = getDataStatusCachable().output.calculated;

  return (
    <div className="grid h-full grid-cols-[auto_1fr] gap-x-8 ">
      <Card className="grid h-0 max-h-full min-h-full min-w-96 grid-rows-[auto_1fr]">
        <CardHeader>
          <CardTitle>Event Details</CardTitle>
          <CardDescription className="w-min min-w-full">
            In dieser Liste sind alle Schritte aufgelistet, die für das Event
            erledigt werden müssen.
          </CardDescription>
        </CardHeader>
        <CardContent className="h-full">
          <div className="flex h-full flex-col justify-between">
            <div>
              <ListTask />
            </div>
            <div className="flex flex-col gap-4">
              <div className="grid grid-cols-[auto_1fr] gap-2">
                <HelpWrapper
                  helpTitle="Ausrechnen"
                  helpDescription="Hilfe zum Button 'Ausrechnen' in den Event Details."
                  helpContent={
                    <div>
                      <p>
                        Durch Klicken auf den Button wird der Algorithmus zur
                        Berechnung der optimalen Eventverteilung gestartet.
                      </p>
                      <br />
                      <p>
                        Die Berechnung kann nur durchgeführt werden, wenn alle
                        Daten hochgeladen wurden.
                      </p>
                      <br />
                      <p>
                        Dieser Schritt kann später rückgängig gemacht werden.
                      </p>
                    </div>
                  }
                />
                <ButtonCalculate disabled={!dataExists || calculationExists} />
              </div>
              <div className="grid grid-cols-[auto_1fr] gap-2">
                <HelpWrapper
                  helpTitle="Zurücksetzen"
                  helpDescription="Hilfe zum Button 'Zurücksetzen' in den Event Details."
                  helpContent={
                    <div>
                      <p>
                        Durch Klicken auf den Button wird die Berechnung der
                        optimalen Eventverteilung zurückgesetzt.
                      </p>
                      <br />
                      <p>
                        Dieser Schritt kann später nicht rückgängig gemacht
                        werden.
                      </p>
                      <br />
                      <p>Die hochgeladenen Daten bleiben erhalten.</p>
                    </div>
                  }
                />
                <ButtonCalculateReset disabled={!calculationExists} />
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <div
        className="grid h-0 max-h-full min-h-full grid-rows-[auto_1fr] items-start justify-stretch
      gap-y-6"
      >
        <MainMenu />
        {props.children}
        {/* <Tabs defaultValue="overview" className="min-h-full flex flex-col">
          <TabsList className="grid  grid-cols-5 gap-x-4 mb-6">
            <TabsTrigger value="overview" className="col-span-2">
              Überischt
            </TabsTrigger>
            <TabsTrigger value="students" asChild>
              <Link href="students"> Schülerliste</Link>
            </TabsTrigger>
            <TabsTrigger value="companies" asChild>
              <Link href="companies">Firmenliste</Link>
            </TabsTrigger>
            <TabsTrigger value="rooms" asChild>
              <Link href="rooms">Raumliste</Link>
            </TabsTrigger>
          </TabsList>
          {props.children}
        </Tabs> */}
      </div>
    </div>
  );
};

export default EventLayout;

export const revalidate = 0;
export const dynamic = "force-dynamic";
