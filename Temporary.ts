export class FeedStore extends IACtorStore {
  private eventFeedList(data = null) {
    return data?.investigationWSEvents?.map(this.transformEvent) || [];
  }

  private transformEvent(event) {
    return {
      sourceEntity: this.getSourceEntity(event),
      sourceOriginalEntity: this.getSourceOriginalEntity(event),
      departmentReceivedDate: this.formatDate(event.sourceData?.departmentReceivedDate),
      finraReceivedDate: this.formatDate(event?.finraReceivedDate),
      type: event?.type,
      lastUpdatedBy: this.getLastUpdatedBy(event),
      lastUpdatedTime: this.getLastUpdatedTime(event),
      summary: event?.summary,
      products: this.transformProducts(event?.products),
      assignees: this.transformAssignees(event.sourceData?.assignees),
      causecodes: this.transformCausecodes(event?.causecodes),
      regulatorySignificance: event?.regulatorySignificance,
      lastUpdatedDate: this.formatDate(event.sourceData?.lastUpdatedDate),
      status: event.sourceData?.status,
      nonRegisteredIndividuals: this.transformIndividuals(event?.nonRegisteredIndividuals),
      nonRegisteredEntities: this.transformEntities(event?.nonRegisteredEntities),
      firms: this.transformFirms(event?.potentialRespondentFirms),
    };
  }

  private getSourceEntity(event) {
    return event.sourceData?.owningDepartment;
  }

  private getSourceOriginalEntity(event) {
    return event.sourceEntity || emptyDoubleDashes;
  }

  private formatDate(date) {
    return date ? formatMMDDYYYY(date) : emptyDoubleDashes;
  }

  private getLastUpdatedBy(event) {
    return event.sourceData?.lastUpdatedBy || emptyDoubleDashes;
  }

  private getLastUpdatedTime(event) {
    return event.sourceData?.lastUpdatedTime || emptyDoubleDashes;
  }

  private transformProducts(products) {
    return products
      ?.filter(item => item?.name?.length > 0 || item?.symbol?.length > 0)
      .map(item => ({
        name: item?.name ? `${item.name} (${appendBracket(item?.symbol)})` : '',
        linkValue: null,
        externalUrl: null,
        nonLinkValue: item,
      })) || [];
  }

  private transformAssignees(assignees) {
    return assignees
      ?.filter(item => item?.isPrimary)
      .map(item => ({
        name: this.getFullName(item?.name),
        linkValue: null,
        externalUrl: null,
        nonLinkValue: item,
      })) || [];
  }

  private getFullName(name) {
    return `${name?.firstName || ''} ${name?.middleName || ''} ${name?.lastName || ''}`.trim();
  }

  private transformCausecodes(causecodes) {
    return causecodes?.map(item => ({
      linkValue: null,
      externalUrl: null,
      nonLinkValue: item,
    })) || [];
  }

  private transformIndividuals(individuals) {
    return individuals?.map(item => ({
      name: this.getFullName(item?.name),
      linkValue: null,
      externalUrl: null,
      nonLinkValue: item,
    })) || [];
  }

  private transformEntities(entities) {
    return entities
      ?.filter(firm => firm?.name?.length > 0)
      .map(firm => ({
        linkValue: null,
        externalUrl: null,
        nonLinkValue: firm.name,
      })) || [];
  }

  private transformFirms(firms) {
    return firms?.map(firm => ({
      nonLinkValue: firm.name,
    })) || [];
  }
}