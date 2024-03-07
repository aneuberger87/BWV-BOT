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

export const CardData = (props: {
  table: {
    header: React.ReactNode;
    body: React.ReactNode;
  };
  title: string;
}) => {
  return (
    <Card className="grid h-full grid-rows-[auto_1fr]">
      <CardHeader>
        <CardTitle>{props.title}</CardTitle>
      </CardHeader>
      <CardContent className="grid h-full grid-rows-[1fr] gap-4 p-6 pt-0">
        <ScrollArea className="h-0 min-h-full">
          <Table className="relative [&_th]:sticky [&_th]:top-0">
            {props.table.header}
            {props.table.body}
          </Table>
        </ScrollArea>
      </CardContent>
    </Card>
  );
};
