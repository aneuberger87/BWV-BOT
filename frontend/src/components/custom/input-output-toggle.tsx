import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import React from "react";

export const InputOutputToggle = (props: { children: React.ReactNode }) => {
  return (
    <Tabs defaultValue="account" className="w-full">
      <TabsList className="absolute right-2 top-2">
        <TabsTrigger value="account">Account</TabsTrigger>
        <TabsTrigger value="password" disabled>
          Password
        </TabsTrigger>
      </TabsList>
      <TabsContent
        value="account"
        className="grid h-full w-full grid-rows-[1fr]"
      >
        {props.children}
      </TabsContent>
      <TabsContent value="password">Change your password here.</TabsContent>
    </Tabs>
  );
};
