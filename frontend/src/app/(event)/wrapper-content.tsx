"use client";

import { TabsContent } from "@/components/ui/tabs";
import { usePathname } from "next/navigation";
import React from "react";

const WrapperContent = (props: { children: React.ReactNode }) => {
  const pathName = usePathname();
  const pathSegments = pathName.split("/");
  const secondSegment = pathSegments?.[2] ?? "undefined";
  console.log("🚀 ~ WrapperContent ~ secondSegment:", secondSegment);

  return <TabsContent value={secondSegment}>{props.children}</TabsContent>;
};

export default WrapperContent;
