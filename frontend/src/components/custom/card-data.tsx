import { excelExists } from "@/lib/excel-exists";
import { ExcelFileName } from "@/types";
import React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import { ScrollArea } from "../ui/scroll-area";
import { Table } from "../ui/table";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const InputOutputToggle = (props: {
  inputChildren: React.ReactNode;
  outputChildren: React.ReactNode;
  disableOutput: boolean;
}) => {
  return (
    <Tabs
      key={`${props.disableOutput}`}
      defaultValue={!props.disableOutput ? "output" : "input"}
      className="w-full"
    >
      <TabsList className="absolute right-2 top-2">
        <TabsTrigger value="input">Input</TabsTrigger>
        <TabsTrigger value="output" disabled={props.disableOutput}>
          Output
        </TabsTrigger>
      </TabsList>
      <TabsContent value="input" className="h-full">
        <div className="grid h-full w-full grid-rows-[1fr]">
          {props.inputChildren}
        </div>
      </TabsContent>
      <TabsContent value="output" className="h-full">
        <div className="grid h-full w-full grid-rows-[1fr]">
          {props.outputChildren}
        </div>
      </TabsContent>
    </Tabs>
  );
};

export const CardData = (props: {
  table: {
    header: React.ReactNode;
    body: React.ReactNode;
  };
  tableOutput?: {
    showDefault: boolean;
    header: React.ReactNode;
    body: React.ReactNode;
  };
  title: string;
  type: ExcelFileName;
}) => {
  const exists = excelExists(props.type);
  return (
    <Card className="relative grid h-full grid-rows-[auto_1fr]">
      <CardHeader>
        <CardTitle>{props.title}</CardTitle>
        {!exists && (
          <CardDescription>
            {props.title} wurde noch nicht hochgeladen.
          </CardDescription>
        )}
      </CardHeader>
      <CardContent className="grid h-full grid-rows-[1fr] gap-4 p-6 pt-0">
        {exists && (
          <InputOutputToggle
            disableOutput={!props.tableOutput}
            inputChildren={
              <ScrollArea className="h-0 min-h-full">
                <Table className="relative [&_th]:sticky [&_th]:top-0">
                  {props.table.header}
                  {props.table.body}
                </Table>
              </ScrollArea>
            }
            outputChildren={
              props.tableOutput && (
                <ScrollArea className="h-0 min-h-full">
                  <Table className="relative [&_th]:sticky [&_th]:top-0">
                    {props.tableOutput.header}
                    {props.tableOutput.body}
                  </Table>
                </ScrollArea>
              )
            }
          />
        )}
      </CardContent>
    </Card>
  );
};
