import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const EventLayout = (props: { children: React.ReactNode }) => {
  return (
    <div className="grid grid-cols-[auto_1fr] h-full gap-x-4">
      <div className="">
        <Card className="h-full grid grid-rows-[auto_1fr]">
          <CardHeader>
            <CardTitle>Event Details</CardTitle>
            <CardDescription>Hier steht der Status oder so</CardDescription>
          </CardHeader>
          <CardContent className="h-full">
            <div className="flex flex-col h-full justify-between">
              <div></div>
              <Button disabled>Auslosen</Button>
            </div>
          </CardContent>
        </Card>
      </div>
      <div className="flex flex-col gap-4">
        <Tabs defaultValue="account" className="w-[400px]">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="account">Schülerliste</TabsTrigger>
            <TabsTrigger value="password">Firmenliste</TabsTrigger>
          </TabsList>
        </Tabs>
        {props.children}
      </div>
    </div>
  );
};

export default EventLayout;
